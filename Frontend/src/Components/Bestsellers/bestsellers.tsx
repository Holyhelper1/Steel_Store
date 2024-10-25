import { ProductCardHit } from "../Product-Card/Product-card-hit";
import styles from "./bestsellers.module.css";
export const Bestsellers = () => {
  return (
    <div className={styles.bestsellers_container}>
      <div className={styles.bestsellers_product_title_hit}>
        <h2>Хиты продаж</h2>
        <p>
          Перейти в каталог <span>&gt;</span>{" "}
        </p>
      </div>
      <div className={styles.bestsellers_product_card_hit}>

      <ProductCardHit />
      <ProductCardHit />
      <ProductCardHit />
      <ProductCardHit />
      </div>
    </div>
  );
};
