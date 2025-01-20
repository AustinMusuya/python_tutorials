const arr = [5, 4, 6, 7, 8, 5, 9, 4, 2, 6, 8, 4];

const target = 2;

const linearSearch = (arr, target) => {
  let indexOfTarget;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] == target) {
      indexOfTarget = arr.indexOf(arr[i]);
    }
  }
  return indexOfTarget;
};

result = linearSearch(arr, target);

console.log(result);
