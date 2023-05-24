project(devtools-arm)

## Setup
cmake_minimum_required(VERSION 3.0)
set(CMAKE_MODULE_PATH "${CMAKE_MODULE_PATH}"
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

include(GNUInstallDirs)

function(install_build_script cmd)
  add_custom_command(OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/${cmd}"
    COMMAND "${CMAKE_COMMAND}" -E make_directory
    "${CMAKE_CURRENT_BINARY_DIR}"
    COMMAND "${CMAKE_COMMAND}" -E create_symlink archbuild
    "${CMAKE_CURRENT_BINARY_DIR}/${cmd}")
  add_custom_target(${cmd}.target ALL
    DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/${cmd}")
  install(FILES "${CMAKE_CURRENT_BINARY_DIR}/${cmd}"
    DESTINATION "${CMAKE_INSTALL_BINDIR}")
endfunction()

function(install_arch CARCH CHOST CARCHFLAGS)
  install_build_script("extra-${CARCH}-build")
  configure_file(pacman-extra.conf.in "extra-${CARCH}.conf" @ONLY)
  configure_file(makepkg.conf.in "${CARCH}.conf" @ONLY)
  install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/extra-${CARCH}.conf"
    DESTINATION "${CMAKE_INSTALL_DATAROOTDIR}/devtools/pacman.conf.d/")
  install(FILES
    "${CMAKE_CURRENT_BINARY_DIR}/${CARCH}.conf"
    DESTINATION "${CMAKE_INSTALL_DATAROOTDIR}/devtools/makepkg.conf.d/")
endfunction()

install_arch(arm armv5tel-unknown-linux-gnueabi "-march=armv5te ")
install_arch(armv6h armv6l-unknown-linux-gnueabihf "-march=armv6 -mfloat-abi=hard -mfpu=vfp ")
install_arch(armv7h armv7l-unknown-linux-gnueabihf "-march=armv7-a -mfloat-abi=hard -mfpu=vfpv3-d16 ")
install_arch(aarch64 aarch64-unknown-linux-gnu "-march=armv8-a ")
