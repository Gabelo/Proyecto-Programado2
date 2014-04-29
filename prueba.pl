restaurante(mac,rapida,cartago,25507334,8-17).
restaurante(mac,rapida,sanjose,22222222,6-22).
restaurante(mac,rapida,belen,45675434,10-20).
restaurante(vishnu,vegetariana,sanjose,22567654,7-18).
restaurante(teriyaki,japonesa,belen,25032134,12-0).
restaurante(bk,rapida,sanjose,26787654,6-23).
restaurante(patito,vegetariana,belen,25034321,8-18).
platillo(mac,bigmac,salado,usa,[pan,carne,queso,lechuga,salsa]).
platillo(mac,applepie,dulce,mexico,[harina,mantequilla,huevos,pure_de_manzana]).
platillo(vishnu,morir_sonando,dulce,costa_rica,[uvas,yogurt,soya]).
platillo(bk,onionrings,agridulce,usa,[cebolla,harina,huevo,aceite]).
platillo(bk,applepie,dulce,japon,[harina,mantequilla,pure]).
prueba(X):-restaurante(X,_,_,_,_).
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
lp(O):-listaplatillos(O).
member(X,[X|Cola]).
member(X,[Cabeza|Cola]):-member(X,Cola).
%member(X):-platillo(Y,Z,A,B,[]).
lp(O,X):-platillo(O,Z,_,_,B),member(X,B),write(Z),nl,fail.


