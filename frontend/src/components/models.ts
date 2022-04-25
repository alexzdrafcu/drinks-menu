export interface Drink {
  id: number;
  image: string;
  name: string;
  description: string;
  category: number;
}

export interface Ingredient {
  id: number;
  quantity: string;
  name: string;
  drink: number;
}

export interface Step {
  id: number;
  name: string;
  description: string;
  drink: number;
}

export enum Categories {
  New = "New",
  SoftDrinks = "Soft Drinks",
  Shots = "Shots",
  Cocktails = "Cocktails",
  BeerAndWine = "Beer&Wine",
  CoffeeAndTea = "Coffee&Tea",
}
