1. 定义在类中的函数默认是内联的。
2. 定义一个默认构造函数就杜绝了一个类型包含未初始化的变量的可能性。
3. 当使用一个 {} 列表时，编译器会创建一个 std::initializer_list 类型。所以可以用此类型当做构造函数等函数的参数。
4. RAII 就是用构造函数分配资源，而用析构函数释放资源。
4. 一个为多种其他类提供接口的类，经常被称作多态类型（polymorphic type）。
5. 通常虚拟类没有构造函数。毕竟，它没有任何需要初始化的数据。同样地，有一个虚拟的析构函数。
6. 接口类必须包含足够的信息，使其在运行时选择正确的函数来调用。通常的实现手法是让编译器将虚函数的名称转化为一个函数指针的表中的索引。该表被称为虚函数表或者 vtbl。每个有虚函数的类都拥有各自的 vtbl 来标识其虚函数。
7. vtbl 中的函数可以被正确使用，即使是在被使用的对象的大小和其数据布局对于被调用者未知的情况下。调用者的实现仅需要知道接口类的 vtbl 中的指针以及每个虚函数的索引。
8. 有继承关系的类的主要的使用方法是指针或引用，而且使用 new 将其实例放在自由存储空间（free store）。
9. 一个函数返回在自由存储空间上分配的对象的指针是很危险的。一个解决方案是返回 unique_ptr。
10. copy constructor, copy assignment, move constructor, move assignment
11. rvalue 就是不能赋值的那些变量之类的。
12. 程序员可以显示地用 std::move 函数来移动变量，在编译器不知道的时候。
13. 在一个层级结构中使用类的默认的 copy 或 move 方法通常会造成灾难：仅仅给定一个基类的指针，我们无法获悉派生类拥有哪些成员，所以我们无法知道如何拷贝它们。所以最好的办法是（在基类中）对与这两类操作关联的方法加上 =delete 后缀。
14. 当用户显式地声明了一个析构函数时，move 操作不会隐式地生成。所以显式地定义析构函数很好。
15. 如果希望用 range-for loop，自定义的类必须有 begin() 和 end() 函数。
16. Function Object，先初始化，然后通过重载的 () 操作符调用。可以和 template 联用，和 lambda 同理。
17. template 的参数数量也可以是可变的
18. 类似 typedef 那样的别名可以用 using 语句。using 可以用来绑定一个 template，然后生成新的 template。
19. 实现继承：共享父类的功能，简化实现开销；接口继承：允许不同的派生类通过共同的基类接口而可互换地被利用。接口继承又称为运行时多态。相对地，通过 template 提供的对多个类的统一使用经常称为编译时多态。
20. 子类的指针可以当作父类的指针使用；子类的引用可以当作父类的引用使用。
21. 将某个类作为父类意味着定义该类的一个（未命名）对象。所以只有已经定义过的类才能作为父类。
22. 引用父类的同名方法要用完全限定名，以免混淆。
23. （只有）虚函数才被称为方法。
24. 非纯虚函数必须在第一次声明它的类中有定义。
25. 即使虚函数所在的类没有派生类，它也能被调用，且一个派生类只需在需要的时候提供其自己的虚函数版本。
26. 派生类中，一个和父类中的虚函数有相同名称和相同参数类型的函数称为基类中对应虚函数的覆盖。返回值可以有更多派生类型。
27. 为了获得运行时多态，被调用的成员函数必须是虚函数且对象必须经由指针或者引用操作。
28. 在构造函数或者析构函数中调用虚函数很不好，但是，如果没有成员在其中，只是调用系统方法呢？
29. 显式地定义覆盖，用 override 关键字，位置是函数声明的末尾。
30. 在 override 的后面加上 final，就禁止后续的继承的覆盖了。如果在派生类的声明中加入 final，则其中所有的覆盖函数都没法再被覆盖了。同时，此类无法再被继承。
31. 函数重载不会超越范围。所以派生类和基类中的同名函数都只存在于各自的类的实例中。可以用基类（可从子类转换）的引用来访问基类中的函数，但是在子类中调用的总是子类的函数。
32. 可以在派生类中使用 using 关键字，来添加基类中的同名函数到派生类，这样子类中就是得到了真正的重载的父类和子类中的同名函数。可以添加构造函数。
33. 派生类访问 protected 成员，只能是自己同类型的实例的成员，不同类型的派生类的 protected 成员不能访问。
34. 将数据成员声明为 protected 非常不好，尽量用 private 修饰；然而用 protected 方法成员却很好。
35. 多重继承，如果多条访问父类的成员的路径造成歧义，则会出错；但是如果没有歧义，比如要访问的成员是 static 的，则可以访问。
36. 如果 using 的语法合法，则可用于扩大成员的使用范围。比如，派生类中，using 基类中的 protected 成员，即使在 public 下也是合法的。其余人则可通过派生类访问这个成员。这对于 private 继承也同样有效。这样可以选择性地只暴露基类的一部分接口。
37. point to member, 形式：::*, ->*, .*, 相当于类中的一个偏移量，可以间接地访问一个类中的成员。
38. 利用 map 分别存储对象的指针和 point to member 的类型，就可以通过字符串的组合来进行不同实例的不同方法的调用。
39. 类的 static 函数可以直接用函数指针，不能用 point to member。
