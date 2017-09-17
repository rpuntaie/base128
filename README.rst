If called from command line, this encodes a binary file into base128.
If imported from python it provides a base128 class to do the same.

An instance of base128 can be used to convert to and from base128 encoding.

Encoding: The python package bitarray is used to insert a 0 bit every 8
bits of the data.  Bitarray cares to shift the bits to make room for the
new bit.  This is done in chunks.  
The length in bits mod 8 can become greater than zero for chunks of size
not equal to a multiple of 7. So ``chunksize`` must be a multiple of 7.
Even if ``chunksize`` is a multiple of 7 the last chunk 
likely has to be padded to reach a multiple of 8 after encoding.
The amount of padding can be expressed as a function of the original data
length mod ``chunksize`` (``modchunk``). ``modchunk`` is added as an
additional byte at the end of the encoding.  To make this byte also
base128, we require ``chunksize``<=128.

If ``chars`` is provided, the resulting 7-bit numbers are 
used as indices to map to entries of ``chars``. 
With bytes ``chars`` the resulting chunks will be integer lists 
and possibly still need to be typed to bytes for further processing::

    with open('tstenc.txt','wb') as f: f.write(b'\n'.join([bytes(x) for x in encoded]))

