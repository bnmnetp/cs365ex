MyClass = function(bv) {

    var myprivatevariable = 100
    this.bar = bv

    this.foo = function() {
	console.log(this.bar)
	baz()
    }
    
    var baz = function() {
	console.log(myprivatevariable)
    }
}

MyClass.prototype.outerfunction = function(a) {
	this.pub = this.bar + a
	return this.pub
}

x = new MyClass(9)


x.foo()
console.log(x.outerfunction(11))



