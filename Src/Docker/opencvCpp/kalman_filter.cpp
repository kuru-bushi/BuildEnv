#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <vector>
#include <opencv2/opencv.hpp>

std::string win = "main";

int h_upper = 115, h_lower = 60;
int s_upper = 255, s_lower = 50;
int v_upper = 200, v_lower = 20;


int main()
{
    cv::VideoCapture cap("your video");
    cv::Mat img_src;
    cv::namedWindow(win);

    cv::KalmanFilter KF(4,2);
    KF.statePre.at<float>(0) = 0;
    KF.statePre.at<float>(1) = 0;
    KF.statePre.at<float>(2) = 0;
    KF.statePre.at<float>(3) = 0;

    // 運動モデル
    KF.transitionMatrix = (cv::Mat_<float>(4,4) << // 等速直線運動
    1, 0, 1, 0,
    0, 1, 0, 0,
    0, 0, 1, 0,
    0, 0, 0, 1);

    cv::setIdentity(KF.measurementMatrix);
    cv::setIdentity(KF.processNoiseCov, cv::Scalar::all(1e-1));
    cv::setIdentity(KF.measurementNoiseCov, cv::Scalar::all(1e-1));
    cv::setIdentity(KF.errorCovPost, cv::Scalar::all(1e-1));

    cv::Mat img_hsv, img_gray, img_gray_th, img_bin, img_lbl, img_dst, img_rgb_th;
    cv::Mat element8 = (cv::Mat_<uchar>(3, 3) << 1, 1, 1, 1, 1, 1, 1, 1, 1);

    while (1) {
        std::vector<cv::Mat> vec_hsv(3);
        cap >> img_src;
        
        // detection tracking object
        cv::cvtColor(img_src, img_gray, cv::COLOR_BGR2GRAY);
        cv::cvtColor(img_src, img_hsv, cv::COLOR_BGR2HSV_FULL);
        cv::split(img_hsv, vec_hsv);
        
        // HSV
        cv::inRange(img_hsv, cv::Scalar(h_lower, s_lower, v_lower), cv::Scalar(h_upper, s_upper, v_upper), img_bin);

        // ノイズ除去
        cv::erode(img_bin, img_bin, element8, cv::Point(-1, -1), 5);
        cv::dilate(img_bin, img_bin, element8, cv::Point(-1, -1), 5);

        // 
        cv::Mat stats, centroids;
        int labelnum = cv::connectedComponentsWithStats(img_bin, img_lbl, stats, centroids);
        if (labelnum == 1) continue;
        long int max_area = 0, max_index = 0;
        for (int i = 1; i < labelnum; i++){
            int area = stats.at<int>(i, cv::CC_STAT_AREA);

            if (area > max_area) {
                max_area = area;
                max_index = i;
            }
        }

        cv::compare(img_lbl, max_index, img_dst, cv::CMP_EQ);

        // 面積最大ラベルの重心
        cv::Moments m = cv::moments(img_dst, true);
        cv::Point pos(m.m10 / m.m00, m.m01 / m.m00);

        // kalmanfilter
        // 観測
        cv::Mat measurement(2, 1, CV_32F);
        measurement.at<float>(0) = pos.x;
        measurement.at<float>(1) = pos.y;        
     } 
    
    
}