## Exporting Fusion 360 design to URDF for ROS2 
If someone is looking for how to export projects from Fusion 360 to URDF, here are the links:
- Original repository (however, it is not maintained and does not work unless you have an older version of Fusion 360): [link](https://github.com/dheena2k2/fusion2urdf-ros2)
- Fork with a merge request that works with the latest Fusion 360 (2.0.20256): [link](https://github.com/Gautham-Ramkumar03/fusion2urdf-ros2/tree/master)

## How to install the plugin
folow the instructions in the original repository to install the plugin. [installing the plugin](https://github.com/dheena2k2/fusion2urdf-ros2?tab=readme-ov-file#installation)

# URDF export procedure
1. Export the project from fusion for which you want to generate urdf files to "step" file In order to do make it easy do delete and move components around withou fusion 360 overhead.
2. Inport the .step file to fusion 360 as new design.
3. Make new component for each rigid set of objects you want to move as one part.
4. Using the selection of bodies ["how to do that"](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-select-all-bodies-in-a-Fusion-360-design.html) copy all bodies for each component to the created components acordingly.
6. Rename the base compenen you will use as the base for the urdf file to "base_link", the other components can be named as you wish. 
5. Making joints between components. In order from last one to the "base_link". if you do th other way aroudn or make a loop the plugin will not work and crash with some vague error.
6. Save the project and make a copy if it because the plugin will make changes to the project. that are hard to revert.
7. Open the copied project and run the plugin. 
8. if some errors occur, try to fix them manually. or look on repo for some solutions.
9. Congratulation you have your urdf files created.

