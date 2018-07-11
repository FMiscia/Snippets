/**
 *
 * Every JS object has the prototype object
 * and inherit its properties and method.
 *
 **/

 // Objects like the followings inherit from Object.prototype
        let x = new Object()
        x = {}

 // Object like:
        x = new Date() // inherits from Date.prototype

// Example
        function Person(first, last, age, eyecolor) {
                this.firstName = first;
                this.lastName = last;
                this.age = age;
                this.eyeColor = eyecolor;
                this.name = function(){ return this.firstName + " " + this.lastName }
        }

        const a = new Person("Simone","DiMarco", 50, "blue")
        const b = new Person("Daniele","Orlando", 30, "green")

//Adding properties to an existing object
        a.nationality = "Italian" //only a has this new property

//Adding properties to the prototype
        Person.nationality = "Italian" //Wrong: prototype is not an existing object
        Person.prototype.nationality = "Italian" //Good: added new property to an existing prototype

//ONLY MODIFY YOUR OWN PROTOTYPES. NEVER MODIFY THE PROTOTYPES OF STANDARD JAVASCRIPT OBJECTS.

// Prototype change (augment this of an object)
        function Animal(...args) {
                this.name = args[0]

                this.getOwner = function() {
                        return this.firstName
                }
        }

        const foo = new Animal("foo")

        Object.setPrototypeOf(foo, a)
        console.log(foo.getOwner())

// How new() works

        function Fruit(...args) {
                this.name = args[0]
        }

        function newInstance(constructor, ...args) {
                // Set the prototype of the constructor function to an empty object
                const ret = Object.setPrototypeOf({}, constructor.prototype)
                // call the constructor over the returning object
                constructor.apply(ret, args)
                // return the ogject
                return ret
        }

        const test = newInstance(Fruit, "apple")

        console.log(test.name)
