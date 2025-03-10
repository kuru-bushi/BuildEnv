#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <opencv2/opencv.hpp>


// フローの表示間隔
#define FLOW_W (10)
#define FLOW_H (10)

std::string wiin_src = "opticalfllow";

int main()
{
    cv::Mat img_pre, img_now;
    cv::Mat img_pre_g, img_now_g;
    cv::Mat flow;

    img_pre = cv::imread("../data/panda_p1.png");
    img_pre = cv::imread("../data/panda_p2.png");

    cv::cvtColor(img_pre, img_pre_g, cv::COLOR_BGR2GRAY);
    cv::cvtColor(img_now, img_now_g, cv::COLOR_BGR2GRAY);

    // initialize
    std::vector<cv::Point2f> ps, pe;
    for (int y = 0; y < img_pre.rows; y+=FLOW_H) {
        for (int x = 0; x < img_pre.cols; x +=FLOW_W) {
            ps.push_back(cv::Point2f(x,y));
        }
    }
    
    // flow calculate
    cv::Mat status, error;
    cv::calcOpticalFlowPyrLK(img_pre_g, img_now_g, ps, pe, status, error);
    
    // flow description
    for (int i = 0; i < ps.size(); i++){
        cv::arrowedLine(img_now, ps[i], pe[i], cv::Scalar(0, 0, 255), 1, 8, 0, 1.0);

    }

    // display
    cv::namedWindow(wiin_src);
    cv::imshow(wiin_src, img_now);

    cv::waitKey(0);
    return 0;
    
}