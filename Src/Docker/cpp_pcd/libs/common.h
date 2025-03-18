#include <iostream>
#include <pcl/io/pcd_io.h>
#include <string>
#include <vector>

    
using CloudType = pcl::PointCloud<pcl::PointXYZ>;
using CloudTypeRGB = pcl::PointCloud<pcl::PointXYZRGB>;


int load_pcd(const std::string path_pcl, CloudType::Ptr &out_cloud)
{
    if (pcl::io::loadPCDFile<pcl::PointXYZ> (path_pcl, *out_cloud) == -1)
    {
        PCL_ERROR("PCDファイルの読み込みに失敗しました。\n");
        return -1;
    }
    return 0;
}

