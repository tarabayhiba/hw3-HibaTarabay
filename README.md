# hw3-HibaTarabay

Homework repo covering two things: a ROS2 pub/sub package and a standalone PCL
(Point Cloud Library) filtering example.

## Repo layout

```
ros2_ws/src/hello_pkg/   ROS2 package with a publisher and subscriber node
pcl_example/             Standalone PCL demo (no ROS2 dependency)
answers.md               Conceptual questions on filtering, PLY formats, outlier removal
```

## ros2_ws — hello_pkg

A minimal ROS2 package with two nodes registered as console scripts.

```bash
cd ros2_ws
colcon build
source install/setup.bash

ros2 run hello_pkg publisher
ros2 run hello_pkg subscriber
```

## pcl_example — voxel_demo

Loads a `.ply` point cloud, drops NaN points, then runs two outlier-removal
filters (`RadiusOutlierRemoval` and `StatisticalOutlierRemoval`), saving each
result back out as a `.ply`. See [pcl_example/commands.txt](pcl_example/commands.txt)
for the full build/run/convert/view command sequence and
[answers.md](answers.md) for the write-up on why each filter behaves the way
it does.

```bash
cd pcl_example
cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build
./build/voxel_demo "data/14 Ladybrook Road 10.ply"
```

This produces `radius_output.ply` and `stat_output.ply` in `pcl_example/`.
Convert to `.pcd` and inspect with `pcl_viewer` using the commands in
[pcl_example/commands.txt](pcl_example/commands.txt) — point cloud data files
(`*.ply`, `*.pcd`) are gitignored since they're regenerable outputs, not source.
