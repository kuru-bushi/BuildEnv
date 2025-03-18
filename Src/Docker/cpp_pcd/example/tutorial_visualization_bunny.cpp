#include <pcl/visualization/cloud_viewer.h>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/common/io.h>
#include <iostream>
#include <thread>
#include <./libs/common.h>


using PCLVisualizer = pcl::visualization::PCLVisualizer;


int main()
{
    // 点群の型定義
    using CloudType = pcl::PointCloud<pcl::PointXYZ>;
    using CloudTypeRGB = pcl::PointCloud<pcl::PointXYZRGB>;

    // 点群のポインタを作成
    CloudType::Ptr original_cloud(new CloudType);
    CloudTypeRGB::Ptr rgb_cloud(new CloudTypeRGB);
    load_pcd("../data/bunny.pcd", original_cloud);

    // pcl::PointXYZからpcl::PointXYZRGBへ変換
    pcl::copyPointCloud(*original_cloud, *rgb_cloud);

    // 各点に赤色を付与
    for (auto& point : rgb_cloud->points)
    {
        point.r = 255;
        point.g = 255;
        point.b = 255;
    }

    // ビューワーの作成 (macOS だと PCLVisualize)
    // pcl::visualization::CloudViewer viewer("PointCloudViewer");
    PCLVisualizer::Ptr vis(new PCLVisualizer);

	vis->addPointCloud(rgb_cloud);
    vis->setPointCloudRenderingProperties(pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 100, "sample cloud");

	// 可視化
	while (!vis->wasStopped()) {
		vis->spinOnce(100);
		std::this_thread::sleep_for(std::chrono::milliseconds(100));
	}
    return 0;
}
