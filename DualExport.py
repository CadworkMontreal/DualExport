# Copyright 2020 Cadwork.
# All rights reserved.
# This file is part of DualExport,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

# import required controllers
import attribute_controller, element_controller, shop_drawing_controller, utility_controller

# get active elements
active_elements = element_controller.get_active_identifiable_element_ids()

# create container list to filter containers
active_containers = []

# filter for containers
for element in active_elements:
  if attribute_controller.is_container(element):
    active_containers.append(element)

# initialize clipboard number
clipboard_number = 0

# disable check and query prompts
utility_controller.push_check_and_query_data()
utility_controller.change_check_and_query_data_to_no_queries()

# loop over containers
for container in active_containers:
  #  export container shop drawing
  single_container_list = [container]
  clipboard_number += 1
  shop_drawing_controller.export_container_with_clipboard(clipboard_number, single_container_list)

  #  get container content
  container_elements = element_controller.get_container_content_elements(container)

  #  export piece-by-piece shop drawing for container content
  clipboard_number += 1
  shop_drawing_controller.export_piece_by_piece_with_clipboard(clipboard_number, container_elements)

# restores check and query prompts
utility_controller.pop_check_and_query_data()

if clipboard_number != 1:
    # display clipboard message to user
  utility_controller.print_error('%d Clipboards Ready...' % clipboard_number)

else:
  # display error message to user
  utility_controller.print_error('Error During Export...')
