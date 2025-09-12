CREATE TABLE IF NOT EXISTS `brukere` (
  `bruker_id` INT NOT NULL AUTO_INCREMENT,
  `passord` TINYBLOB NOT NULL,
  `fornavn` NVARCHAR(75) NOT NULL,
  `etternavn` NVARCHAR(75) NOT NULL,
  `tlf` INT NULL,
  `epost` NVARCHAR(75) NOT NULL,
  `fodselsdato` DATE NOT NULL,
  `postnr` INT NULL,
  `adresse` NVARCHAR(100) NULL,
  PRIMARY KEY (`bruker_id`));
  
CREATE TABLE IF NOT EXISTS `mydb`.`oppforinger` (
  `oppforing_id` INT NOT NULL AUTO_INCREMENT,
  `selger_id` INT NOT NULL,
  `produktnavn` NVARCHAR(100) NOT NULL,
  `beskrivelse` NVARCHAR(4000) NULL,
  `pris` DECIMAL(7,2) NOT NULL,
  `sist_endret` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `bilde` NVARCHAR(150) NULL,
  PRIMARY KEY (`oppforing_id`),
  INDEX `fk_oppforinger_brukere1_idx` (`selger_id` ASC) VISIBLE,
  CONSTRAINT `fk_oppforinger_brukere1`
    FOREIGN KEY (`selger_id`)
    REFERENCES `mydb`.`brukere` (`bruker_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
CREATE TABLE IF NOT EXISTS `mydb`.`produkter` (
  `produkt_id` INT NOT NULL AUTO_INCREMENT,
  `oppforing` INT NOT NULL,
  `produktnavn` NVARCHAR(100) NOT NULL,
  `spesifikasjon` VARCHAR(2000) NULL,
  PRIMARY KEY (`produkt_id`),
  INDEX `fk_produkter_oppforinger1_idx` (`oppforing` ASC) VISIBLE,
  CONSTRAINT `fk_produkter_oppforinger1`
    FOREIGN KEY (`oppforing`)
    REFERENCES `mydb`.`oppforinger` (`oppforing_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);