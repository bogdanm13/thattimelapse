# This is not a Makefile

timestamp:=$(shell date +%s)

test_camera:
	python3 camera.py

timelapse: save_previous do_timelapse generate_video
	echo "Done!"

save_previous:
	mv capture/timelapse capture/timelapse-$(timestamp)

do_timelapse:
	python3 timelapse.py

generate_video:
	echo "Pass!"
