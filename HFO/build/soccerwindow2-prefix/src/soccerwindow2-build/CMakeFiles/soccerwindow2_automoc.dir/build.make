# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.2

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2-build

# Utility rule file for soccerwindow2_automoc.

# Include the progress variables for this target.
include CMakeFiles/soccerwindow2_automoc.dir/progress.make

CMakeFiles/soccerwindow2_automoc:
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2-build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Automatic moc for target soccerwindow2"
	/usr/bin/cmake -E cmake_autogen /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2-build/CMakeFiles/soccerwindow2_automoc.dir/ Release

soccerwindow2_automoc: CMakeFiles/soccerwindow2_automoc
soccerwindow2_automoc: CMakeFiles/soccerwindow2_automoc.dir/build.make
.PHONY : soccerwindow2_automoc

# Rule to build all files generated by this target.
CMakeFiles/soccerwindow2_automoc.dir/build: soccerwindow2_automoc
.PHONY : CMakeFiles/soccerwindow2_automoc.dir/build

CMakeFiles/soccerwindow2_automoc.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/soccerwindow2_automoc.dir/cmake_clean.cmake
.PHONY : CMakeFiles/soccerwindow2_automoc.dir/clean

CMakeFiles/soccerwindow2_automoc.dir/depend:
	cd /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2 /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2 /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2-build /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2-build /home/leno/HFO/build/soccerwindow2-prefix/src/soccerwindow2-build/CMakeFiles/soccerwindow2_automoc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/soccerwindow2_automoc.dir/depend

