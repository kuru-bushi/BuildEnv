#include <thread>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/pcl_visualizer.h>

using PointXYZ = pcl::PointXYZ;
using PointXYZRGB = pcl::PointXYZRGB;
using CloudXYZRGB = pcl::PointCloud<PointXYZRGB>;
using PCLVisualizer = pcl::visualization::PCLVisualizer;

PointXYZ to_PointXYZ(const PointXYZRGB& point) {
	
	PointXYZ p(point.x, point.y, point.z);
	return p;
}

int main() {

	CloudXYZRGB::Ptr cloud(new CloudXYZRGB);
	CloudXYZRGB::Ptr end_points(new CloudXYZRGB);
	for (int x = 0; x < 10; x++) {
		PointXYZRGB point;
		point.x = x;
		point.r = 255;
		point.g = 255;
		point.b = 255;
		cloud->push_back(point);

		// y方向にずらす
		if (x == 3 || x == 6) {
			point.y = 1.0;
			end_points->push_back(point);
		}
	}

	PCLVisualizer::Ptr vis(new PCLVisualizer);

	// 点群クラスを追加
	vis->addPointCloud(cloud);

	// 球を追加
	vis->addSphere(to_PointXYZ(end_points->at(0)), 0.20, 1.0, 1.0, 0.0, "s1");
	vis->addSphere(to_PointXYZ(end_points->at(1)), 0.20, 1.0, 0.0, 1.0, "s2");

	// 線を追加
	vis->addLine(to_PointXYZ(end_points->at(0)), to_PointXYZ(end_points->at(1)), 0.0, 1.0, 1.0, "line1");

	// 可視化
	while (!vis->wasStopped()) {
		vis->spinOnce(100);
		std::this_thread::sleep_for(std::chrono::milliseconds(100));
	}

	return 0;
}