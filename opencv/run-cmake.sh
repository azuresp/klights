mkdir /tmp/opencv-4.0.1/build
cd /tmp/opencv-4.0.1/build

cmake \
-D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D INSTALL_PYTHON_EXAMPLES=ON \
-D OPENCV_EXTRA_MODULES_PATH=/tmp/opencv_contrib-4.0.1/modules \
-D BUILD_EXAMPLES=ON ..
