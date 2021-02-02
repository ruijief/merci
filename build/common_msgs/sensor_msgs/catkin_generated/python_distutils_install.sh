#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/zzk/kai_ws/mercedes_ws/src/common_msgs/sensor_msgs"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/zzk/kai_ws/mercedes_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/zzk/kai_ws/mercedes_ws/install/lib/python2.7/dist-packages:/home/zzk/kai_ws/mercedes_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/zzk/kai_ws/mercedes_ws/build" \
    "/usr/bin/python2" \
    "/home/zzk/kai_ws/mercedes_ws/src/common_msgs/sensor_msgs/setup.py" \
    egg_info --egg-base /home/zzk/kai_ws/mercedes_ws/build/common_msgs/sensor_msgs \
    build --build-base "/home/zzk/kai_ws/mercedes_ws/build/common_msgs/sensor_msgs" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/zzk/kai_ws/mercedes_ws/install" --install-scripts="/home/zzk/kai_ws/mercedes_ws/install/bin"
