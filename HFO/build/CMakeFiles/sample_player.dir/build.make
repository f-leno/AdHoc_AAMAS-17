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
CMAKE_SOURCE_DIR = /home/leno/HFO

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/leno/HFO/build

# Include any dependencies generated for this target.
include CMakeFiles/sample_player.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/sample_player.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/sample_player.dir/flags.make

CMakeFiles/sample_player.dir/src/HFO.cpp.o: CMakeFiles/sample_player.dir/flags.make
CMakeFiles/sample_player.dir/src/HFO.cpp.o: ../src/HFO.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/sample_player.dir/src/HFO.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/sample_player.dir/src/HFO.cpp.o -c /home/leno/HFO/src/HFO.cpp

CMakeFiles/sample_player.dir/src/HFO.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sample_player.dir/src/HFO.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/leno/HFO/src/HFO.cpp > CMakeFiles/sample_player.dir/src/HFO.cpp.i

CMakeFiles/sample_player.dir/src/HFO.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sample_player.dir/src/HFO.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/leno/HFO/src/HFO.cpp -o CMakeFiles/sample_player.dir/src/HFO.cpp.s

CMakeFiles/sample_player.dir/src/HFO.cpp.o.requires:
.PHONY : CMakeFiles/sample_player.dir/src/HFO.cpp.o.requires

CMakeFiles/sample_player.dir/src/HFO.cpp.o.provides: CMakeFiles/sample_player.dir/src/HFO.cpp.o.requires
	$(MAKE) -f CMakeFiles/sample_player.dir/build.make CMakeFiles/sample_player.dir/src/HFO.cpp.o.provides.build
.PHONY : CMakeFiles/sample_player.dir/src/HFO.cpp.o.provides

CMakeFiles/sample_player.dir/src/HFO.cpp.o.provides.build: CMakeFiles/sample_player.dir/src/HFO.cpp.o

CMakeFiles/sample_player.dir/src/main_player.cpp.o: CMakeFiles/sample_player.dir/flags.make
CMakeFiles/sample_player.dir/src/main_player.cpp.o: ../src/main_player.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/sample_player.dir/src/main_player.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/sample_player.dir/src/main_player.cpp.o -c /home/leno/HFO/src/main_player.cpp

CMakeFiles/sample_player.dir/src/main_player.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sample_player.dir/src/main_player.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/leno/HFO/src/main_player.cpp > CMakeFiles/sample_player.dir/src/main_player.cpp.i

CMakeFiles/sample_player.dir/src/main_player.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sample_player.dir/src/main_player.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/leno/HFO/src/main_player.cpp -o CMakeFiles/sample_player.dir/src/main_player.cpp.s

CMakeFiles/sample_player.dir/src/main_player.cpp.o.requires:
.PHONY : CMakeFiles/sample_player.dir/src/main_player.cpp.o.requires

CMakeFiles/sample_player.dir/src/main_player.cpp.o.provides: CMakeFiles/sample_player.dir/src/main_player.cpp.o.requires
	$(MAKE) -f CMakeFiles/sample_player.dir/build.make CMakeFiles/sample_player.dir/src/main_player.cpp.o.provides.build
.PHONY : CMakeFiles/sample_player.dir/src/main_player.cpp.o.provides

CMakeFiles/sample_player.dir/src/main_player.cpp.o.provides.build: CMakeFiles/sample_player.dir/src/main_player.cpp.o

CMakeFiles/sample_player.dir/src/sample_player.cpp.o: CMakeFiles/sample_player.dir/flags.make
CMakeFiles/sample_player.dir/src/sample_player.cpp.o: ../src/sample_player.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/sample_player.dir/src/sample_player.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/sample_player.dir/src/sample_player.cpp.o -c /home/leno/HFO/src/sample_player.cpp

CMakeFiles/sample_player.dir/src/sample_player.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sample_player.dir/src/sample_player.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/leno/HFO/src/sample_player.cpp > CMakeFiles/sample_player.dir/src/sample_player.cpp.i

CMakeFiles/sample_player.dir/src/sample_player.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sample_player.dir/src/sample_player.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/leno/HFO/src/sample_player.cpp -o CMakeFiles/sample_player.dir/src/sample_player.cpp.s

CMakeFiles/sample_player.dir/src/sample_player.cpp.o.requires:
.PHONY : CMakeFiles/sample_player.dir/src/sample_player.cpp.o.requires

CMakeFiles/sample_player.dir/src/sample_player.cpp.o.provides: CMakeFiles/sample_player.dir/src/sample_player.cpp.o.requires
	$(MAKE) -f CMakeFiles/sample_player.dir/build.make CMakeFiles/sample_player.dir/src/sample_player.cpp.o.provides.build
.PHONY : CMakeFiles/sample_player.dir/src/sample_player.cpp.o.provides

CMakeFiles/sample_player.dir/src/sample_player.cpp.o.provides.build: CMakeFiles/sample_player.dir/src/sample_player.cpp.o

CMakeFiles/sample_player.dir/src/agent.cpp.o: CMakeFiles/sample_player.dir/flags.make
CMakeFiles/sample_player.dir/src/agent.cpp.o: ../src/agent.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/sample_player.dir/src/agent.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/sample_player.dir/src/agent.cpp.o -c /home/leno/HFO/src/agent.cpp

CMakeFiles/sample_player.dir/src/agent.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sample_player.dir/src/agent.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/leno/HFO/src/agent.cpp > CMakeFiles/sample_player.dir/src/agent.cpp.i

CMakeFiles/sample_player.dir/src/agent.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sample_player.dir/src/agent.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/leno/HFO/src/agent.cpp -o CMakeFiles/sample_player.dir/src/agent.cpp.s

CMakeFiles/sample_player.dir/src/agent.cpp.o.requires:
.PHONY : CMakeFiles/sample_player.dir/src/agent.cpp.o.requires

CMakeFiles/sample_player.dir/src/agent.cpp.o.provides: CMakeFiles/sample_player.dir/src/agent.cpp.o.requires
	$(MAKE) -f CMakeFiles/sample_player.dir/build.make CMakeFiles/sample_player.dir/src/agent.cpp.o.provides.build
.PHONY : CMakeFiles/sample_player.dir/src/agent.cpp.o.provides

CMakeFiles/sample_player.dir/src/agent.cpp.o.provides.build: CMakeFiles/sample_player.dir/src/agent.cpp.o

# Object files for target sample_player
sample_player_OBJECTS = \
"CMakeFiles/sample_player.dir/src/HFO.cpp.o" \
"CMakeFiles/sample_player.dir/src/main_player.cpp.o" \
"CMakeFiles/sample_player.dir/src/sample_player.cpp.o" \
"CMakeFiles/sample_player.dir/src/agent.cpp.o"

# External object files for target sample_player
sample_player_EXTERNAL_OBJECTS =

teams/base/sample_player: CMakeFiles/sample_player.dir/src/HFO.cpp.o
teams/base/sample_player: CMakeFiles/sample_player.dir/src/main_player.cpp.o
teams/base/sample_player: CMakeFiles/sample_player.dir/src/sample_player.cpp.o
teams/base/sample_player: CMakeFiles/sample_player.dir/src/agent.cpp.o
teams/base/sample_player: CMakeFiles/sample_player.dir/build.make
teams/base/sample_player: libplayer_chain_action.a
teams/base/sample_player: CMakeFiles/sample_player.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable teams/base/sample_player"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sample_player.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/sample_player.dir/build: teams/base/sample_player
.PHONY : CMakeFiles/sample_player.dir/build

CMakeFiles/sample_player.dir/requires: CMakeFiles/sample_player.dir/src/HFO.cpp.o.requires
CMakeFiles/sample_player.dir/requires: CMakeFiles/sample_player.dir/src/main_player.cpp.o.requires
CMakeFiles/sample_player.dir/requires: CMakeFiles/sample_player.dir/src/sample_player.cpp.o.requires
CMakeFiles/sample_player.dir/requires: CMakeFiles/sample_player.dir/src/agent.cpp.o.requires
.PHONY : CMakeFiles/sample_player.dir/requires

CMakeFiles/sample_player.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/sample_player.dir/cmake_clean.cmake
.PHONY : CMakeFiles/sample_player.dir/clean

CMakeFiles/sample_player.dir/depend:
	cd /home/leno/HFO/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/leno/HFO /home/leno/HFO /home/leno/HFO/build /home/leno/HFO/build /home/leno/HFO/build/CMakeFiles/sample_player.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/sample_player.dir/depend

