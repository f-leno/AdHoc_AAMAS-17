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
CMAKE_SOURCE_DIR = /home/leno/HFO/build/rcssserver-prefix/src/rcssserver

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build

# Include any dependencies generated for this target.
include CMakeFiles/rcssconfparser.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/rcssconfparser.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/rcssconfparser.dir/flags.make

CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o: CMakeFiles/rcssconfparser.dir/flags.make
CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o: /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/statushandler.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o -c /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/statushandler.cpp

CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/statushandler.cpp > CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.i

CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/statushandler.cpp -o CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.s

CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o.requires:
.PHONY : CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o.requires

CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o.provides: CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o.requires
	$(MAKE) -f CMakeFiles/rcssconfparser.dir/build.make CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o.provides.build
.PHONY : CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o.provides

CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o.provides.build: CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o

CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o: CMakeFiles/rcssconfparser.dir/flags.make
CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o: /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/parser.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o -c /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/parser.cpp

CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/parser.cpp > CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.i

CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/parser.cpp -o CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.s

CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o.requires:
.PHONY : CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o.requires

CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o.provides: CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o.requires
	$(MAKE) -f CMakeFiles/rcssconfparser.dir/build.make CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o.provides.build
.PHONY : CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o.provides

CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o.provides.build: CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o

CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o: CMakeFiles/rcssconfparser.dir/flags.make
CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o: /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/streamstatushandler.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o -c /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/streamstatushandler.cpp

CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/streamstatushandler.cpp > CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.i

CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/streamstatushandler.cpp -o CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.s

CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o.requires:
.PHONY : CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o.requires

CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o.provides: CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o.requires
	$(MAKE) -f CMakeFiles/rcssconfparser.dir/build.make CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o.provides.build
.PHONY : CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o.provides

CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o.provides.build: CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o

CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o: CMakeFiles/rcssconfparser.dir/flags.make
CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o: /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/builder.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o -c /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/builder.cpp

CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/builder.cpp > CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.i

CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/leno/HFO/build/rcssserver-prefix/src/rcssserver/rcssbase/conf/builder.cpp -o CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.s

CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o.requires:
.PHONY : CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o.requires

CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o.provides: CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o.requires
	$(MAKE) -f CMakeFiles/rcssconfparser.dir/build.make CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o.provides.build
.PHONY : CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o.provides

CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o.provides.build: CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o

# Object files for target rcssconfparser
rcssconfparser_OBJECTS = \
"CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o" \
"CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o" \
"CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o" \
"CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o"

# External object files for target rcssconfparser
rcssconfparser_EXTERNAL_OBJECTS =

lib/librcssconfparser.a: CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o
lib/librcssconfparser.a: CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o
lib/librcssconfparser.a: CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o
lib/librcssconfparser.a: CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o
lib/librcssconfparser.a: CMakeFiles/rcssconfparser.dir/build.make
lib/librcssconfparser.a: CMakeFiles/rcssconfparser.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX static library lib/librcssconfparser.a"
	$(CMAKE_COMMAND) -P CMakeFiles/rcssconfparser.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rcssconfparser.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/rcssconfparser.dir/build: lib/librcssconfparser.a
.PHONY : CMakeFiles/rcssconfparser.dir/build

CMakeFiles/rcssconfparser.dir/requires: CMakeFiles/rcssconfparser.dir/rcssbase/conf/statushandler.cpp.o.requires
CMakeFiles/rcssconfparser.dir/requires: CMakeFiles/rcssconfparser.dir/rcssbase/conf/parser.cpp.o.requires
CMakeFiles/rcssconfparser.dir/requires: CMakeFiles/rcssconfparser.dir/rcssbase/conf/streamstatushandler.cpp.o.requires
CMakeFiles/rcssconfparser.dir/requires: CMakeFiles/rcssconfparser.dir/rcssbase/conf/builder.cpp.o.requires
.PHONY : CMakeFiles/rcssconfparser.dir/requires

CMakeFiles/rcssconfparser.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/rcssconfparser.dir/cmake_clean.cmake
.PHONY : CMakeFiles/rcssconfparser.dir/clean

CMakeFiles/rcssconfparser.dir/depend:
	cd /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/leno/HFO/build/rcssserver-prefix/src/rcssserver /home/leno/HFO/build/rcssserver-prefix/src/rcssserver /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build /home/leno/HFO/build/rcssserver-prefix/src/rcssserver-build/CMakeFiles/rcssconfparser.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/rcssconfparser.dir/depend

