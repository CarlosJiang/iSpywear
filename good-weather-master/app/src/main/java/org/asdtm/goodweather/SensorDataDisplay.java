
package org.asdtm.goodweather;

import android.Manifest;
import android.app.Activity;
import android.content.pm.PackageManager;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Environment;
import android.support.v4.app.ActivityCompat;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

import com.microsoft.band.BandClient;
import com.microsoft.band.BandClientManager;
import com.microsoft.band.BandException;
import com.microsoft.band.BandIOException;
import com.microsoft.band.BandInfo;
import com.microsoft.band.ConnectionState;
import com.microsoft.band.sensors.BandAccelerometerEvent;
import com.microsoft.band.sensors.BandAccelerometerEventListener;
import com.microsoft.band.sensors.BandGyroscopeEvent;
import com.microsoft.band.sensors.BandGyroscopeEventListener;
import com.microsoft.band.sensors.SampleRate;



import java.io.File;
import java.io.RandomAccessFile;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import static android.os.Environment.DIRECTORY_DOWNLOADS;

public class SensorDataDisplay extends BaseActivity implements View.OnClickListener {

    private BandClient client = null;
    private Button btnStart, btnStopWrite;
    private Boolean doWrite = false;
    private TextView txtStatus,gyroStatus;
    private TextView mTextView;
    private String sensorData, Acc_sensorData, Gyro_sensorData;
    // Storage Permissions
    private static final int REQUEST_EXTERNAL_STORAGE = 1;
    private static String[] PERMISSIONS_STORAGE = {
            Manifest.permission.READ_EXTERNAL_STORAGE,
            Manifest.permission.WRITE_EXTERNAL_STORAGE
    };



    private BandAccelerometerEventListener mAccelerometerEventListener = new BandAccelerometerEventListener() {
        @Override
        public void onBandAccelerometerChanged(BandAccelerometerEvent bandAccelerometerEvent) {
            if (bandAccelerometerEvent != null) {
                appendToUI(String.format(" Acc.X = %.3f \n Acc.Y = %.3f\n Acc.Z = %.3f", bandAccelerometerEvent.getAccelerationX(),
                        bandAccelerometerEvent.getAccelerationY(), bandAccelerometerEvent.getAccelerationZ()));
            }

            DecimalFormat df = new DecimalFormat("#,##0.000000");
            SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss.SSS");
            String str = sdf.format(new Date());
            Acc_sensorData = str + "," + df.format(bandAccelerometerEvent.getAccelerationX()) + "," + df.format(bandAccelerometerEvent.getAccelerationY()) + "," + df.format(bandAccelerometerEvent.getAccelerationZ());
//            if (doWrite) {
//                writeFileSdcard(Acc_sensorData);
//            }
        }
    };

    private BandGyroscopeEventListener mGyroscopeEventListener = new BandGyroscopeEventListener() {
        @Override
        public void onBandGyroscopeChanged(final BandGyroscopeEvent bandGyroscopeEvent) {
            if (bandGyroscopeEvent != null) {
                appendToGyro(String.format("\n Gyro.X = %.3f \n Gyro.Y = %.3f\n Gyro.Z = %.3f", bandGyroscopeEvent.getAngularVelocityX(),
                        bandGyroscopeEvent.getAngularVelocityY(), bandGyroscopeEvent.getAngularVelocityZ()));
            }

            DecimalFormat df = new DecimalFormat("#,##0.000000");
            SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss.SSS");
            String str = sdf.format(new Date());
            Gyro_sensorData  =df.format(bandGyroscopeEvent.getAngularVelocityX()) + "," + df.format(bandGyroscopeEvent.getAngularVelocityY()) + "," + df.format(bandGyroscopeEvent.getAngularVelocityZ()) + "," + "0" + "\n";
            sensorData = Acc_sensorData + "," + Gyro_sensorData;
            if (doWrite) {
                writeFileSdcard(sensorData);
            }

        }
    };


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sensor_data_display);

        btnStopWrite = (Button) findViewById(R.id.btnStop);
        btnStopWrite.setOnClickListener(this);
        mTextView = (TextView)findViewById(R.id.txtStatus);

        txtStatus = (TextView) findViewById(R.id.txtGeneralDis);
        gyroStatus = (TextView) findViewById(R.id.txtGyroData);
        btnStart = (Button) findViewById(R.id.btnStart);
        verifyStoragePermissions(this);
        btnStart.setOnClickListener(new OnClickListener() {
            @Override
            public void onClick(View v) {
                getSdCardPath();
                new AccelerometerSubscriptionTask().execute();
                new BandGyroscopeSubscriptionTask().execute();
                doWrite = true;
            }
        });
    }

    public static void verifyStoragePermissions(Activity activity) {
        // Check if we have write permission
        int permission = ActivityCompat.checkSelfPermission(activity, Manifest.permission.WRITE_EXTERNAL_STORAGE);

        if (permission != PackageManager.PERMISSION_GRANTED) {
            // We don't have permission so prompt the user
            ActivityCompat.requestPermissions(
                    activity,
                    PERMISSIONS_STORAGE,
                    REQUEST_EXTERNAL_STORAGE
            );
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
    }


    private void writeFileSdcard(String message) {
        try {
            // 如果手机插入了SD卡，而且应用程序具有访问SD的权限
            if (Environment.getExternalStorageState().equals(Environment.MEDIA_MOUNTED)) {
                // 获取SD卡的目录
                File sdCardDir = Environment.getExternalStoragePublicDirectory(DIRECTORY_DOWNLOADS);
                File targetFile = new File(sdCardDir.getCanonicalPath() + "/SensorData"+"test.txt");
                // 以指定文件创建 RandomAccessFile对象
                RandomAccessFile raf = new RandomAccessFile(targetFile, "rw");
                // 将文件记录指针移动到最后
                raf.seek(targetFile.length());
                // 输出文件内容
                raf.write(message.getBytes());
                // 关闭RandomAccessFile
                raf.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (client != null) {
            try {
                client.getSensorManager().unregisterAccelerometerEventListener(mAccelerometerEventListener);
                client.getSensorManager().unregisterGyroscopeEventListener(mGyroscopeEventListener);
            } catch (BandIOException e) {
                appendToUI(e.getMessage());
            }
        }
    }

    private class BandGyroscopeSubscriptionTask extends AsyncTask<Void, Void, Void>{
        @Override
        protected Void doInBackground(Void... params) {
            try {
                if (getConnectedBandClient()) {
                    appendToUI("Band is connected.\n");
                    client.getSensorManager().registerGyroscopeEventListener(mGyroscopeEventListener,SampleRate.MS128);
                } else {
                    appendToUI("Band isn't connected. Please make sure bluetooth is on and the band is in range.\n");
                }
            } catch (BandException e) {
                String exceptionMessage="";
                switch (e.getErrorType()) {
                    case UNSUPPORTED_SDK_VERSION_ERROR:
                        exceptionMessage = "Microsoft Health BandService doesn't support your SDK Version. Please update to latest SDK.\n";
                        break;
                    case SERVICE_ERROR:
                        exceptionMessage = "Microsoft Health BandService is not available. Please make sure Microsoft Health is installed and that you have the correct permissions.\n";
                        break;
                    default:
                        exceptionMessage = "Unknown error occured: " + e.getMessage() + "\n";
                        break;
                }
                appendToUI(exceptionMessage);

            } catch (Exception e) {
                appendToUI(e.getMessage());
            }
            return null;
        }
    }


    private class AccelerometerSubscriptionTask extends AsyncTask<Void, Void, Void> {
        @Override
        protected Void doInBackground(Void... params) {
            try {
                if (getConnectedBandClient()) {
                    appendToUI("Band is connected.\n");
                    client.getSensorManager().registerAccelerometerEventListener(mAccelerometerEventListener, SampleRate.MS128);
                } else {
                    appendToUI("Band isn't connected. Please make sure bluetooth is on and the band is in range.\n");
                }
            } catch (BandException e) {
                String exceptionMessage="";
                switch (e.getErrorType()) {
                    case UNSUPPORTED_SDK_VERSION_ERROR:
                        exceptionMessage = "Microsoft Health BandService doesn't support your SDK Version. Please update to latest SDK.\n";
                        break;
                    case SERVICE_ERROR:
                        exceptionMessage = "Microsoft Health BandService is not available. Please make sure Microsoft Health is installed and that you have the correct permissions.\n";
                        break;
                    default:
                        exceptionMessage = "Unknown error occured: " + e.getMessage() + "\n";
                        break;
                }
                appendToUI(exceptionMessage);

            } catch (Exception e) {
                appendToUI(e.getMessage());
            }
            return null;
        }
    }

    @Override
    protected void onDestroy() {
        if (client != null) {
            try {
                client.disconnect().await();
            } catch (InterruptedException e) {
                // Do nothing as this is happening during destroy
            } catch (BandException e) {
                // Do nothing as this is happening during destroy
            }
        }
        super.onDestroy();
    }

    private void appendToUI(final String string) {
        this.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                txtStatus.setText(string);
            }
        });
    }
    private void appendToGyro(final String string) {
        this.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                gyroStatus.setText(string);
            }
        });
    }

    private boolean getConnectedBandClient() throws InterruptedException, BandException {
        if (client == null) {
            BandInfo[] devices = BandClientManager.getInstance().getPairedBands();
            if (devices.length == 0) {
                appendToUI("Band isn't paired with your phone.\n");
                return false;
            }
            client = BandClientManager.getInstance().create(getBaseContext(), devices[0]);
        } else if (ConnectionState.CONNECTED == client.getConnectionState()) {
            return true;
        }

        appendToUI("Band is connecting...\n");
        return ConnectionState.CONNECTED == client.connect().await();
    }


    public void onClick(View v) {
        if (v.getId() == R.id.btnStart) {
            doWrite = true;
            mTextView.setText("Status：Writing");
        }
        if (v.getId() == R.id.btnStop) {
            doWrite = false;
            mTextView.setText("Status：stop");
        }
    }


    /**
     * If sd card exists
     *
     * @return
     */
    public static boolean isSdCardExist() {
        return Environment.getExternalStorageState().equals(
                Environment.MEDIA_MOUNTED);
    }

    /**
     * Get SD card root directory
     *
     * @return
     */
    public static String getSdCardPath() {
        boolean exist = isSdCardExist();
        String sdpath = "";
        if (exist) {
            sdpath = Environment.getExternalStorageDirectory()
                    .getAbsolutePath();
        } else {
            sdpath = "不适用";
        }
        return sdpath;

    }
    /**
     * Checks if the app has permission to write to device storage
     *
     * If the app does not has permission then the user will be prompted to grant permissions
     *
     * @param activity
     */


}

