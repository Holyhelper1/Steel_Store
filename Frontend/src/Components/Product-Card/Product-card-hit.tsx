import styles from "./product-card.module.css";
import product_card_img from "./assets/Fox1.png";
import { Button } from "../Button/Button";
import Stars from "./assets/Star 1.png";
import Scales from "./assets/Scales.png";
import Heart from "./assets/heart.png";
import CartWight from "../Button/assets/Cart.png";

export const ProductCardHit = () => {
  return (
    <div className={styles.product_card_container}>
      <div className={styles.product_card_img}>
        <img src={product_card_img} alt="product_card_img" />
      </div>
      <div className={styles.product_card_title}>
        <h2>Нож Лиса</h2>
      </div>
      <div className={styles.product_card_info}>
        <div className={styles.product_size}>95x18</div>
        <div className={styles.product_material}>Орех, Алюминий</div>
      </div>

      <div className={styles.product_reviews}>
        <div className={styles.product_card_stars}>
          <img src={Stars} alt="Stars" />
          <img src={Stars} alt="Stars" />
          <img src={Stars} alt="Stars" />
          <img src={Stars} alt="Stars" />
          <img src={Stars} alt="Stars" />
        </div>
        <div className={styles.product_number_reviews}>12 отзывов </div>
      </div>
      <div className={styles.product_card_hr_line}></div>

      <div className={styles.product_card_price}>
        <div className={styles.product_card_price_current}>2 719 р.</div>
        <div className={styles.product_compare_button}>
          <img src={Scales} alt="Scales" />
          <img src={Heart} alt="Heart" />
        </div>
      </div>

      <Button>В корзину &nbsp; &nbsp; <img src={CartWight} alt="Cart" /></Button>
    </div>
  );
};
