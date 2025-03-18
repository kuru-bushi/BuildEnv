#include <pcl/visualization/cloud_viewer.h>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/common/io.h>
#include <iostream>
#include <thread>
#include <./libs/common.h>

#include <random>
#include <pcl/point_types.h>
#include <pcl/features/normal_3d.h>


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


    pcl::NormalEstimation<pcl::PointXYZ, pcl::Normal> ne;
    ne.setInputCloud(original_cloud);
    // ne.setInputCloud(rgb_cloud); // error/

    pcl::search::KdTree<pcl::PointXYZ>::Ptr tree (new pcl::search::KdTree<pcl::PointXYZ> ());
    ne.setSearchMethod(tree);
    
    pcl::PointCloud<pcl::Normal>::Ptr cloud_normals (new pcl::PointCloud<pcl::Normal>);

    // Use all neighbors in a sphere of radius 3cm
    ne.setRadiusSearch(0.03);

    // Compute the features
    ne.compute(*cloud_normals);
    std::mt19937 rand_gen(1);

    // ビューワーの作成 (macOS だと PCLVisualizer が動作)
    // pcl::visualization::CloudViewer viewer("PointCloudViewer");
    PCLVisualizer::Ptr vis(new PCLVisualizer);


    for (int i = 0; i < 10; i++) {
    // for (int i = 0; i < cloud_normals->size(); i++) {

		int id = rand_gen() % cloud_normals->width;

		pcl::PointXYZRGB point = rgb_cloud->at(id);
		pcl::Normal normal = cloud_normals->at(id);

		Eigen::Vector3f end_vf(point.x, point.y, point.z);
		Eigen::Vector3f normal_vf(normal.normal_x, normal.normal_y, normal.normal_z);
		Eigen::Vector3f start_vf = end_vf + normal_vf;

		pcl::PointXYZ start = pcl::PointXYZ(start_vf.x(), start_vf.y(), start_vf.z());
		pcl::PointXYZ end = pcl::PointXYZ(end_vf.x(), end_vf.y(), end_vf.z());

		vis->addArrow(start, end, 1.0, 1.0, 1.0, false, "a" + std::to_string(i));
    }

	vis->addPointCloud(rgb_cloud);
    vis->setPointCloudRenderingProperties(pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 100, "sample cloud");

	// 可視化
	while (!vis->wasStopped()) {
		vis->spinOnce(100);
		std::this_thread::sleep_for(std::chrono::milliseconds(100));
	}
    return 0;
}
