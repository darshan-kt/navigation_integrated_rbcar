### Rbcar Navigation Package 

This package provides a comprehensive simulation and navigation stack for the Rbcar robot model. It integrates the rbcar metapackage and a customized version of the teb_local_planner for precise local path planning and navigation.
📦 Package Contents

    rbcar metapackage
    Includes all essential components to simulate the Rbcar robot, including:

        Vehicle model

        Gazebo simulation world

        Mapping tools

        Localization using AMCL (Adaptive Monte Carlo Localization)

    teb_local_planner
    A fine-tuned version of the Timed Elastic Band local planner optimized for the Rbcar model, providing smooth and efficient path planning in dynamic environments.

#### Launch Instructions

To start the full simulation environment including the Gazebo world, robot model, controllers, and navigation stack, run the following command:
```bash
roslaunch rbcar_localization amcl_with_movebase.launch
```
This will:

    Spawn the Rbcar in a simulated Gazebo world

    Start all necessary robot controllers

    Launch AMCL for localization

    Start move_base with the customized teb_local_planner

#### Navigation

Once everything is running:

    Open Rviz.

    Use the "2D Nav Goal" tool to set a target pose within the map.

    The Rbcar will plan and follow a path to the goal using the tuned TEB planner.
