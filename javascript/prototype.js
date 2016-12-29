/**
 * 
 * Every JS object has the prototype object
 * and inherit its properties and method.
 * 
 **/

 // Objects like the followings inherit from Object.prototype
        var x = new Object() 
        var x = {} 
 
 // Object like:
        var x = new Date() // inherits from Date.prototype

// Example
        function Person(first, last, age, eyecolor) {
                this.firstName = first;
                this.lastName = last;
                this.age = age;
                this.eyeColor = eyecolor;
                this.name = function(){ return this.firstName + " " + this.lastName }
        }

        var a = new Person("Simone","DiMarco", 50, "blue")
        var b = new Person("Daniele","Orlando", 30, "green")

//Adding properties to an existing object
        a.nationality = "Italian" //only a has this new property
        
//Adding properties to the prototype
        Person.nationality = "Italian" //Wrong: prototype is not an existing object
        Person.prototype.nationality = "Italian" //Good: added new property to an existing prototype

//ONLY MODIFY YOUR OWN PROTOTYPES. NEVER MODIFY THE PROTOTYPES OF STANDARD JAVASCRIPT OBJECTS.

