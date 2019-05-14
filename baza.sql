drop database if exists projekt;
create database projekt character set utf8;

use projekt;

create table mjerenja(
sifra int not null PRIMARY KEY auto_increment,
temperature decimal(5,2) not null,
vlaga tinyint not null,
tlak_zraka decimal(5,1) not null,
baterija smallint not null


);


create table korisnici(
sifra int not null PRIMARY KEY auto_increment


);