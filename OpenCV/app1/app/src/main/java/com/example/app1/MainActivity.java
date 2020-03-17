package com.example.app1;

import android.Manifest;
import android.app.Activity;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.Toast;

import androidx.annotation.NonNull;

import com.theartofdev.edmodo.cropper.CropImage;
import com.theartofdev.edmodo.cropper.CropImageView;

import org.opencv.android.OpenCVLoader;
import org.opencv.android.Utils;
import org.opencv.core.CvException;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.MatOfPoint;
import org.opencv.core.Scalar;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class MainActivity extends Activity
{
    private static final int CAMERA_REQUEST = 1888;
    private ImageView imageView;
    private Bitmap photo;
    private Bitmap currentBitmap;
    private static final int MY_CAMERA_PERMISSION_CODE = 100;

    static {
        if (!OpenCVLoader.initDebug()) {
            // Handle initialization error
            Log.e("msg","Initialized!");
        }
        else{
            Log.e("msg","Sorry, not initialized!");
        }
    }

    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        this.imageView = (ImageView)this.findViewById(R.id.imagecode);
        Button capButton = (Button) this.findViewById(R.id.capbtn);
        Button anaButton = (Button) this.findViewById(R.id.analyzeButton);
        capButton.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                    if (checkSelfPermission(Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED)
                    {
                        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                            requestPermissions(new String[]{Manifest.permission.CAMERA}, MY_CAMERA_PERMISSION_CODE);
                        }
                    }
                    else
                    {
//                        Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
//                        startActivityForResult(cameraIntent, CAMERA_REQUEST);

                        CropImage.activity()
                                .setGuidelines(CropImageView.Guidelines.ON)
                                .start(MainActivity.this);
                    }
                }
            }
        });

        anaButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(photo == null){
                    Toast.makeText(MainActivity.this,"Not Captured the image",Toast.LENGTH_LONG);
                }
                Mat originalMat = new Mat();
                Utils.bitmapToMat(photo,originalMat);
                Mat grayMat = new Mat();
                Mat imgBlur = new Mat();
                Mat cannyEdges = new Mat();
                Mat hierarchy = new Mat();
                List<MatOfPoint> contourList = new ArrayList<MatOfPoint>(); //A list to store all the contours

                /* My try





                 */
                final Size ksize = new Size(5,5);
                Imgproc.cvtColor(originalMat, grayMat, Imgproc.COLOR_BGR2GRAY);
                Imgproc.GaussianBlur(grayMat,imgBlur,ksize, 1);
                Imgproc.Canny(imgBlur, cannyEdges, 10, 50);
                Imgproc.findContours(cannyEdges, contourList, hierarchy, Imgproc.RETR_EXTERNAL, Imgproc.CHAIN_APPROX_NONE);
                //Drawing contours on a new image
                Mat contours = new Mat();
//                contours.create(cannyEdges.rows(), cannyEdges.cols(), CvType.CV_8UC3);
                originalMat.copyTo(contours);
                Random r = new Random();
//                cv2.drawContours(imgContours,countours,-1,(0,255,0),1)
                for (int i = 0; i < contourList.size(); i++) {
                    Imgproc.drawContours(contours, contourList, i, new Scalar(0,255,0), 1);
                }
                Bitmap bmp = null;
                Mat rgb = new Mat();
                Imgproc.cvtColor(contours, rgb, Imgproc.COLOR_BGR2RGB);

                try {
                    bmp = Bitmap.createBitmap(rgb.cols(), rgb.rows(), Bitmap.Config.ARGB_8888);
                    Utils.matToBitmap(rgb, bmp);
                    imageView.setImageBitmap(bmp);
                }
                catch (CvException e){
                    Log.d("Exception",e.getMessage());
                }
            }
        });


    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults)
    {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (requestCode == MY_CAMERA_PERMISSION_CODE)
        {
            if (grantResults[0] == PackageManager.PERMISSION_GRANTED)
            {
                Toast.makeText(this, "camera permission granted", Toast.LENGTH_LONG).show();
                Intent cameraIntent = new Intent(android.provider.MediaStore.ACTION_IMAGE_CAPTURE);
                startActivityForResult(cameraIntent, CAMERA_REQUEST);
            }
            else
            {
                Toast.makeText(this, "camera permission denied", Toast.LENGTH_LONG).show();
            }
        }
    }

    private Bitmap decodeUri(Uri selectedImage) throws FileNotFoundException {

        // Decode image size
        BitmapFactory.Options o = new BitmapFactory.Options();
        o.inJustDecodeBounds = true;
        BitmapFactory.decodeStream(getContentResolver().openInputStream(selectedImage), null, o);

        // The new size we want to scale to
        final int REQUIRED_SIZE = 140;

        // Find the correct scale value. It should be the power of 2.
        int width_tmp = o.outWidth, height_tmp = o.outHeight;
        int scale = 1;
        while (true) {
            if (width_tmp / 2 < REQUIRED_SIZE
                    || height_tmp / 2 < REQUIRED_SIZE) {
                break;
            }
            width_tmp /= 2;
            height_tmp /= 2;
            scale *= 2;
        }

        // Decode with inSampleSize
        BitmapFactory.Options o2 = new BitmapFactory.Options();
        o2.inSampleSize = scale;
        return BitmapFactory.decodeStream(getContentResolver().openInputStream(selectedImage), null, o2);

    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data)
    {

        if (requestCode == CropImage.CROP_IMAGE_ACTIVITY_REQUEST_CODE) {

            CropImage.ActivityResult result = CropImage.getActivityResult(data);

            photo = (Bitmap) result.getBitmap();
            if (resultCode == RESULT_OK) {
                Uri resultUri = result.getUri();
                imageView.setImageURI(resultUri);

                //From here you can load the image however you need to, I recommend using the Glide library

//                Uri resultUri = result.getUri();
//                imageView.setImageURI(resultUri);
                try {
                    photo = decodeUri(resultUri);
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                }
            } else if (resultCode == CropImage.CROP_IMAGE_ACTIVITY_RESULT_ERROR_CODE) {
                Exception error = result.getError();
            }
        }
    }


}