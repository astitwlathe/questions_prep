#!/bin/bash
if ! grep -q "^deb .*http://packages.ros.org/ros/ubuntu.*" /etc/apt/sources.list /etc/apt/sources.list.d/*; then
	echo "Setting up your computer to accept software from packages.ros.org"
	sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
	sudo apt -y install curl # if you haven't already installed curl
	curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
	

fi
sudo apt update
sudo apt -y install ros-noetic-desktop-full
if ! grep -q "source /opt/ros/noetic/setup.bash.*" ~/.bashrc; then
	echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
	source ~/.bashrc

fi
sudo apt -y install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo apt -y install python3-catkin-tools
sudo rosdep init
rosdep update

sudo apt install -y vim

rm -rf ~/dependencies_ws/

mkdir ~/dependencies_ws
mkdir ~/dependencies_ws/src
cd ~/dependencies_ws/src
git clone git@gitlab.cs.washington.edu:cse478/23wi/cse478_dependencies.git --recurse-submodules
cd cse478_dependencies/
rosdep install --from-paths . --ignore-src -y -r
cd ~/dependencies_ws
catkin build
