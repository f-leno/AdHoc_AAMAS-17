.PHONY : tiles

tiles: tiles.so

tilesInt.o: tilesInt.C
	c++ -fno-strict-aliasing -Wno-long-double -mno-fused-madd -fno-common -dynamic -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/home/leno/anaconda2/include/python2.7 -c tilesInt.C -o tilesInt.o -fPIC

tiles.o: tiles.cpp
	c++ -fno-strict-aliasing -Wno-long-double -mno-fused-madd -fno-common -dynamic -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -I/home/leno/anaconda2/include/python2.7 -c tiles.cpp -o tiles.o -fPIC

tiles.so: tiles.o tilesInt.o
	#c++ -Wl,-F. -Wl,-F. -shared Python tiles.o tilesInt.o -o tiles.so -I/home/leno/anaconda2/include/python2.7 -lpython2.7
	c++ -Wl,-F. -Wl,-F. -shared tiles.o tilesInt.o -o tiles.so -I/home/leno/anaconda2/include/python2.7 -lpython2.7
