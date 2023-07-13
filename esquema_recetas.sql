-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_recetas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_recetas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_recetas` DEFAULT CHARACTER SET utf8 ;
USE `esquema_recetas` ;

-- -----------------------------------------------------
-- Table `esquema_recetas`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_recetas`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(145) NULL,
  `apellido` VARCHAR(145) NULL,
  `email` VARCHAR(145) NULL,
  `password` VARCHAR(255) NULL,
  `creado` DATETIME NULL DEFAULT NOW(),
  `editado` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_recetas`.`recetas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_recetas`.`recetas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(145) NOT NULL,
  `descripcion` LONGTEXT NOT NULL,
  `instrucciones` LONGTEXT NOT NULL,
  `menos_de_treinta` BINARY NOT NULL,
  `fecha_cocinado` DATETIME NOT NULL,
  `creado` DATETIME NOT NULL DEFAULT NOW(),
  `editado` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `id_usuario` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recetas_usuarios_idx` (`id_usuario` ASC) VISIBLE,
  CONSTRAINT `fk_recetas_usuarios`
    FOREIGN KEY (`id_usuario`)
    REFERENCES `esquema_recetas`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
