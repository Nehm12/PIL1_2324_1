CREATE DATABASE if not exists rqt;
USE rqt;

CREATE TABLE if not exists User (
    id INT,
    primary key (id),
    name VARCHAR(100)
   
);
-- Création de la table Interest
CREATE TABLE  if not exists interest (
    id INT AUTO_INCREMENT ,
    PRIMARY KEY(id),
    gender CHAR(1) NOT NULL,
    min_age INT NOT NULL,
    max_age INT NOT NULL,
    localisation varchar(100),
    CHECK (gender IN ('M', 'F'))
);

-- Création de la table Profile
CREATE TABLE if not exists profile (
    id INT AUTO_INCREMENT,
    PRIMARY KEY(id),
    User_id INT NOT NULL unique ,
    bio varchar(100),
    sexe varchar(1),
    age INT NOT NULL,
    location VARCHAR(100) NOT NULL,
    FOREIGN KEY (User_id) REFERENCES User(id) ON DELETE CASCADE
);

-- Table intermédiaire pour la relation Many-to-Many entre Profile et Interest
CREATE TABLE if not exists profile_interests (
    profile_id INT NOT NULL,
    interest_id INT NOT NULL,
    PRIMARY KEY (profile_id, interest_id),
    FOREIGN KEY (profile_id) REFERENCES profile(id) ON DELETE CASCADE,
    FOREIGN KEY (interest_id) REFERENCES interest(id) ON DELETE CASCADE
);
create table message(
	id INT,
	primary key(id),
	user1_id INT NOT null unique,
	user2_id INT NOT null unique,
    foreign key(user1_id) references user(id) on delete cascade,
	foreign key(user2_id) references user(id) on delete cascade,
    content varchar(255),
    heure time,
    jour date
    )