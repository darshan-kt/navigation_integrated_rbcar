# navigation_integrated_rabcar
This package includes rbcar metapackage and teb_local_planner


This package has rbcar metapackage for rbcar vehicle model, gazebo world, mapping, localization. For navigation of rbcar model is done by using fine tuned teb_local_planner.

Launch the below launch file, it will launches the entire world, car, controllers and navigation stack.
$ roslaunch rbcar_localization amcl_with_movebase.launch

Then provide the target pose inside the map using Rviz 2D Nav Goal.
