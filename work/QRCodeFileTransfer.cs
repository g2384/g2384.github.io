/*
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="OpenCvSharp4" Version="4.9.0.20240103" />
    <PackageReference Include="OpenCvSharp4.Extensions" Version="4.9.0.20240103" />
    <PackageReference Include="OpenCvSharp4.runtime.win" Version="4.9.0.20240103" />
    <PackageReference Include="System.Drawing.Common" Version="8.0.2" />
    <PackageReference Include="ZXing.Net" Version="0.16.9" />
  </ItemGroup>

</Project>
*/

using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using OpenCvSharp;
using ZXing;
using ZXing.Common;

namespace QRCodeFileTransfer
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Store unique QR codes
            HashSet<string> uniqueQRCodes = new();

            // Initialize the camera
            using var capture = new VideoCapture(0);
            if (!capture.IsOpened())
            {
                Console.WriteLine("Error: Could not access the camera.");
                return;
            }

            // Configure camera properties
            capture.Set(VideoCaptureProperties.FrameWidth, 640);
            capture.Set(VideoCaptureProperties.FrameHeight, 480);

            // Create window to show camera feed
            Cv2.NamedWindow("QR Scanner");

            // Use a reader instance (MultiFormatReader works with BinaryBitmap)
            var reader = new MultiFormatReader();

            Console.WriteLine("QR Code Scanner started. Press 'Esc' to exit.");

            while (true)
            {
                using var frame = new Mat();
                capture.Read(frame);

                if (frame.Empty())
                    continue;

                // Convert OpenCV Mat to byte array for ZXing
                int bytes = (int)(frame.Total() * frame.ElemSize());
                byte[] rawBytes = new byte[bytes];
                Marshal.Copy(frame.Data, rawBytes, 0, bytes);

                // Try to decode QR code using a BinaryBitmap
                try
                {
                    var luminanceSource = new RGBLuminanceSource(rawBytes, frame.Cols, frame.Rows, RGBLuminanceSource.BitmapFormat.BGR24);
                    var binaryBitmap = new BinaryBitmap(new HybridBinarizer(luminanceSource));
                    var result = reader.decode(binaryBitmap);

                    if (result != null)
                    {
                        string qrText = result.Text;
                        if (qrText.Contains("filename", StringComparison.OrdinalIgnoreCase))
                        {
                            if (uniqueQRCodes.Add(qrText))
                            {
                                Console.WriteLine($"New QR Code detected: {qrText}");

                                // Draw rectangle around the QR code if points available
                                var points = result.ResultPoints;
                                if (points != null && points.Length >= 2)
                                {
                                    // Draw a rectangle using the first two points as opposite corners
                                    var p0 = new OpenCvSharp.Point((int)points[0].X, (int)points[0].Y);
                                    var p1 = new OpenCvSharp.Point((int)points[1].X, (int)points[1].Y);
                                    Cv2.Rectangle(frame, p0, p1, Scalar.Green, 2);
                                }
                            }
                        }
                    }
                }
                catch (Exception ex)
                {
                    // Ignore decode errors and continue
                    Console.Error.WriteLine($"Decode error: {ex.Message}");
                }

                // Show the frame
                Cv2.ImShow("QR Scanner", frame);

                // Check for escape key to exit
                int key = Cv2.WaitKey(1);
                if (key == 27) // ESC key
                    break;
            }

            // Cleanup
            Cv2.DestroyAllWindows();
        }
    }
}

