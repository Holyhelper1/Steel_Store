import { SearchBar } from "../Header/Search_bar/Search_bar";
import { ChooserHeader } from "../Product-Chooser/Chooser-header/Chooser-header";
import { ChooserInfo } from "../Product-Chooser/Chooser-info/Chooser-info";
import { ProductCard } from "../Product/Product-card";
import styles from "./main.module.css";
import Knife1 from "../Product/assets/knife-1.png";
import Knife2 from "../Product/assets/knife-2.png";
import Knife3 from "../Product/assets/knife-3.png";
import Knife4 from "../Product/assets/knife-4.png";
import Knife5 from "../Product/assets/knife-5.png";
import Knife7 from "../Product/assets/knife-7.png";
import { Bestsellers } from "../Bestsellers/bestsellers";

const mokProductsData = [
  {
    id: 1,
    title: "Каталог ножей",
    image: Knife1,
  },
  {
    id: 2,
    title: "Средне клинковое оружие",
    image: Knife2,
  },
  {
    id: 3,
    title: "Длинно клинковое оружие",
    image: Knife3,
  },
  {
    id: 4,
    title: "Сувенирные изделия",
    image: Knife4,
  },
  {
    id: 5,
    title: "Сопутствующие товары",
    image: Knife5,
  },
  {
    id: 6,
    title: "Ножевая мастерская",
    image: Knife7,
  },
];

export const Main = () => {
  return (
    <div>
      <SearchBar />
      <ChooserHeader />
      <ChooserInfo />
      <div className={styles.main_product_container}>
        {mokProductsData.map((product) => (
          <ProductCard key={product.id} products={[product]} />
        ))}
      </div>
    <Bestsellers/>
    </div>
  );
};
