#include <iostream>
#include <pcl/io/ply_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/filter.h>
#include <pcl/io/pcd_io.h>
#include <pcl/filters/radius_outlier_removal.h>
#include <pcl/filters/statistical_outlier_removal.h>

// If you wish to get rid of the squiggly line you will need to generate compile_commands.json
// in cmake and symlink it to the root of this repo. You can use clangd or c++ intellisense extension
// (Recommended to make your life easier, and preferably use clangd, will prompt you to install a 
// clangd binary in vscode and disable intellisense).
// Check with AI if you need help.


int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "Usage: ./demo input.ply\n";
        return 1;
    }

    // Load as XYZRGB
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZRGB>);
    if (pcl::io::loadPLYFile<pcl::PointXYZRGB>(argv[1], *cloud) == -1) {
        PCL_ERROR("Could not read file\n");
        return -1;
    }
    std::cout << "Loaded: " << cloud->size() << " points\n";

    std :: vector < int > indices ;
    pcl :: removeNaNFromPointCloud (* cloud , * cloud , indices ) ;
    std::cout << "After NaN removal: " << cloud->size() << "\n";

    // Inspect the first point -- check if RGB actually loaded
    if (!cloud->empty()) {
        auto& p = cloud->points[0];
        std::cout << "First point: x=" << p.x
                  << " y=" << p.y
                  << " z=" << p.z
                  << " r=" << int(p.r)
                  << " g=" << int(p.g)
                  << " b=" << int(p.b) << "\n";
    }

        // radius outlier removal
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr radius_cloud(new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::RadiusOutlierRemoval<pcl::PointXYZRGB> ror;
    ror.setInputCloud(cloud);
    ror.setRadiusSearch(0.05);
    ror.setMinNeighborsInRadius(5);
    ror.filter(*radius_cloud);
    std::cout << "After RadiusOutlierRemoval: " << radius_cloud->size() << " points\n";
    pcl::io::savePLYFileBinary("radius_output.ply", *radius_cloud);

    // stats outlier removal
    pcl::PointCloud<pcl::PointXYZRGB>::Ptr stat_cloud(new pcl::PointCloud<pcl::PointXYZRGB>);
    pcl::StatisticalOutlierRemoval<pcl::PointXYZRGB> sor;
    sor.setInputCloud(cloud);
    sor.setMeanK(50);
    sor.setStddevMulThresh(1.0);
    sor.filter(*stat_cloud);
    std::cout << "After StatisticalOutlierRemoval: " << stat_cloud->size() << " points\n";
    pcl::io::savePLYFileBinary("stat_output.ply", *stat_cloud);


    return 0;
}


