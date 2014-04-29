tc(X):-restaurante(Y,X,_,_,_),write(Y). %%Escribe el nombre del restaurante que coincide con un tipo de comida.
listatipocomida(Z):-tc(Z),nl,fail. %%Imprime la lista de restaurantes que coinciden con un tipo de comida especifica
ltc(A):-listatipocomida(A). %%abreviatura de la regla anterior
bn(X):-restaurante(X,_,Z,_,_),write(Z). %%Busca ubicacion de restaurante de acuerdo a nombre.
listarestaurantesnombre(C):-bn(C),nl,fail. %%Imprime toda la lista de ubicacion de restaurantes de acuerdo al nombre.
lrn(A):-listarestaurantesnombre(A).
lr:-write('nombre,tipocomida,ubicacion,telefono,horario'),nl,listarestaurantes.
listarestaurantes:-restaurante(X,Y,Z,A,B),write(restaurante(X,Y,Z,A,B)),nl,fail.
listaplatillos(X):-platillo(Y,_,_,X,_),write(Y),nl,fail. %lista de restaurantes que tienen platillo de un pais especifico
listaplatillos(X):-platillo(X,Y,_,_,_),write(Y),nl,fail. %lista de platillos de un restaurante especifico.
lp(O):-listaplatillos(O).%lista platillos
member(X,[X|Cola]).%determina si es miembro y esta al inicio de la lista
member(X,[Cabeza|Cola]):-member(X,Cola).%determina si es miembro al no estar en el inicio de la lista
lp(O,X):-platillo(O,Z,_,_,B),member(X,B),write(Z),nl,fail. %lista de platillos que son de un restaurante determinado y tienen un ingrediente determinado
