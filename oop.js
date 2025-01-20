class Dog {
  #name;
  constructor(name) {
    this.#name = name;
    this._behavior = 0;
  }

  get name() {
    return this.#name;
  }
  get behavior() {
    return this._behavior;
  }

  incrementBehavior() {
    this._behavior++;
  }
}

const dog1 = new Dog("Luffy");

// console.log(dog1);

console.log(dog1.name);
