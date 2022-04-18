script_path=`realpath "$0"`
script_dir=`dirname "$script_path"`
$script_dir/build-cache.sh
$script_dir/exited-containers.sh
