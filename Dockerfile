FROM harmish/morse:ros

RUN apt-get update && \
    # install pr2 and naviagation packages
    apt-get install -y \
        ros-$ROS_DISTRO-navigation \
        ros-$ROS_DISTRO-gmapping \
        ros-$ROS_DISTRO-robot-state-publisher \
        ros-$ROS_DISTRO-pr2-common \
        ros-$ROS_DISTRO-pr2-controllers \
        ros-$ROS_DISTRO-pr2-mechanism \
        ros-$ROS_DISTRO-pr2-navigation \
        ros-$ROS_DISTRO-pr2-common-actions \
        ros-$ROS_DISTRO-pr2-teleop && \

    # fix for tuck-arms
    git clone https://github.com/harmishhk/pr2_common_actions.git -b indigo-devel /pr2_ws/src/pr2_common_actions && \
    bash -c "source /opt/ros/indigo/setup.bash && catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/indigo -C /pr2_ws install" && \

    # clean-up
    rm -rf /pr2_ws && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

VOLUME /catkin_ws
COPY . /catkin_ws/src/
    # install morse-ros packages
RUN bash -c "source /opt/ros/indigo/setup.bash && catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/indigo -C /catkin_ws install"
