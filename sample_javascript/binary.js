const arr = [5, 4, 6, 7, 8, 5, 9, 4, 2, 6, 8, 4];

const target = 2;

// Hash Map search
function searchWithHash(arr, target) {
  const hashTable = {};
  for (let i = 0; i < arr.length; i++) {
    hashTable[arr[i]] = i;
  }

  // Directly check if the target exists in the hash table
  if (hashTable[target] !== undefined) {
    return hashTable[target]; // Return the index of the target
  }

  // Return -1 if the target is not found
  return -1;
}

const result = searchWithHash(arr, target);

// console.log(result);

// Linear search

const linearSearch = (arr, target) => {
  let indexOfTarget;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
      indexOfTarget = arr.indexOf(arr[i]);
    }
  }
  return indexOfTarget;
};

result1 = linearSearch(arr, target);

console.log(result1);
