#include <iostream>
#include <thread>
#include <random>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <pcl/filters/voxel_grid.h>
#include <./libs/common.h>


#include <cassert>
#include <algorithm>
#include <functional>

using PointXYZRGB = pcl::PointXYZRGB;

using CloudXYZRGB = pcl::PointCloud<PointXYZRGB>;
using PCLVisualizer = pcl::visualization::PCLVisualizer;

int main() {
	

    CloudType::Ptr original_cloud(new CloudType);
	CloudXYZRGB::Ptr filtered_cloud(new CloudXYZRGB);
    CloudTypeRGB::Ptr rgb_cloud(new CloudTypeRGB);

	const double leaf_size = 0.5;

    load_pcd("../data/bunny.pcd", original_cloud);
    pcl::copyPointCloud(*original_cloud, *rgb_cloud);

    // 各点に赤色を付与
    for (auto& point : rgb_cloud->points)
    {
        point.r = 255;
        point.g = 255;
        point.b = 255;
    }

	pcl::VoxelGrid<PointXYZRGB>::Ptr grid(new pcl::VoxelGrid<PointXYZRGB>);
	grid->setInputCloud(rgb_cloud);
	grid->setLeafSize(leaf_size, leaf_size, leaf_size);
	grid->setSaveLeafLayout(true);
	grid->filter(*filtered_cloud);


	std::cout << "before : " << rgb_cloud->width << std::endl;
	std::cout << "after  : " << filtered_cloud->width << std::endl;

	const double shift_x = 1.0;

	PCLVisualizer::Ptr vis(new PCLVisualizer);
	vis->addPointCloud(rgb_cloud, "1");
	vis->addPointCloud(filtered_cloud, "2");

    // ボクセルを走査（maxも範囲に含みます）
	std::vector<float> radius(filtered_cloud->width);
    for (int i =std::min(0); i <= std::max(0); i++) {
		for (int j = std::min(1); j <= std::max(1); j++) {
			for (int k = std::min(2); k <= std::max(2); k++) {
				Eigen::Vector3i ijk(i, j, k);
				int cloud_index = grid->getCentroidIndexAt(ijk);
				if (cloud_index != VOXEL_GRID_EMPTY) {
					radius[cloud_index] = 0.050 * (i + j + k + 1);
				}
			}
		}
	}

    // 可視化
	while (!vis->wasStopped()) {
		// vis->spinOnce(100);
        vis->addSphere(to_PointXYZ(filtered_cloud->at(i)), radius[i], 1.0, 1.0, 1.0, std::to_string(i));
		std::this_thread::sleep_for(std::chrono::milliseconds(100));
	}
	return 0;
}
