def new(num_buckets=256):
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	#print("hash_key:",hash(key),",len:",len(aMap)," ,",hash(key) % len(aMap))
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	bucketId = hash_key(aMap, key)
	return aMap[bucketId]

def get_slot(aMap, key, default = None):
	bucket = get_bucket(aMap,key)
	#print("get_slot——enumerate:",enumerate(bucket))
	for i , kv in enumerate(bucket):
		print("get_slot", i, " ", kv, " bucket:", bucket)
		k , v = kv
		#print("get_slot::", k, " " , v)
		if key == k:
			return i, k , v
	return -1, key , default

def get(aMap, key, default=None):
	"""Gets the value in a bucket for the given key, or the default."""
	i, k, v = get_slot(aMap, key, default)
	return v

def set(aMap, key, value):
	#print("""Sets the key to the value, replacing any existing value.""")
	bucket = get_bucket(aMap, key)
	#print("set_bucket:",bucket)
	i, k, v = get_slot(aMap, key)
	if i >=0:
		bucket[i] = (key, value)
	else:
		bucket.append((key,value))
		
def delete(aMap, key):
	"""Deletes the given key from the Map."""
	bucket = get_bucket(aMap, key)
	for i in range(len(bucket)):
		k, v = bucket[i]
		if key == k :
			del bucket[i]
			break
			
def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		#print("list:", bucket)
		if bucket:
			for k, v in bucket:
				print(k,v)