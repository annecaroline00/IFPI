CREATE TABLE "categoria" (
  "cod_categoria" smallint,
  "descricao " varchar[20],
  PRIMARY KEY ("cod_categoria")
);

CREATE TABLE "livro" (
  "isbn" varchar[13],
  "titulo" varchar [20],
  "ano" smallint,
  "editora" varchar [30],
  "cod_categoria" varchar[30],
  PRIMARY KEY ("isbn"),
  CONSTRAINT "FK_livro.cod_categoria"
    FOREIGN KEY ("cod_categoria")
      REFERENCES "categoria"("descricao ")
);

CREATE TABLE "autor" (
  "nome" varchar(30),
  "nacionalidade" varchar(20),
  "cod_autor" smallint,
  PRIMARY KEY ("cod_autor")
);

CREATE TABLE "autor_livro" (
  "cod_autor" smallint,
  "isbn" varchar[13],
  PRIMARY KEY ("cod_autor", "isbn"),
  CONSTRAINT "FK_autor_livro.isbn"
    FOREIGN KEY ("isbn")
      REFERENCES "livro"("isbn"),
  CONSTRAINT "FK_autor_livro.cod_autor"
    FOREIGN KEY ("cod_autor")
      REFERENCES "autor"("cod_autor")
);

