**Q1.** If you applied a filter and the output had unexpected NaN points, why could that happen? What should you do before running any filter?

NaN points can appear in filter output if the input point cloud from sensors or other sources already has NaN values (invalid coordinate values) that the filter didn't remove, or if the filter encountered invalid data during processing. Additionally, uninitialized memory or sensor artifacts can introduce NaN values during intermediate calculations. Before applying any filter, validation and cleaning input data by removing or handling any existing NaN values using methods like removeNaNFromPointCloud() is important

**Q2.** What is the difference between `savePLYFileASCII` and `savePLYFileBinary`? When would you prefer one over the other?

`savePLYFileASCII` saves data as human readable text which makes files larger but easier to inspect and edit manually. `savePLYFileBinary` compresses the data into binary format which creates much smaller files that are faster to read & write. ASCII is preferred for debugging and sharing human readable data, or sharing data with collaborators who don't have PCL installed. Binary is superior when file size and I/O speed matters for example: production workflows, large point clouds (millions+ points), especially in real-time robotics or autonomous systems



**Q3.** PCL has a filter called `RadiusOutlierRemoval`. What does it do and how is it different from `StatisticalOutlierRemoval`?

Both filters aim to remove noise & outliers.

`RadiusOutlierRemoval` removes points that have fewer than k neighbors within a fixed radius, it's a distance based approach. Radius removal uses a fixed spatial threshold, making it rigid but predictable. 

`StatisticalOutlierRemoval` removes points whose average distance to neighbors significantly exceeds the mean distance of the entire cloud, it's a statistics based approach. This results in a slightly slower computation, assumes Gaussian like distribution of distances which may not work well if outliers dominate the dataset. Also requires tuning the standard deviation multiplier


Radius removal is better for uniformly dense clouds, while statistical removal adapts to varying point densities across regions.
use cases: `RadiusOutlierRemoval` on LiDAR scans with consistent scanning patterns or uniformly dense data. `StatisticalOutlierRemoval` on heterogeneous data, or reconstructed point clouds