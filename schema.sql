drop table if exists accounts;
    create table accounts (
    id integer primary key autoincrement,
    username text not null,
    email text not null, 
    password text not null
);