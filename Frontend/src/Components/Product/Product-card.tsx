import styles from "./product-card.module.css";
// import Product_image from "./assets/knife-1.png";

interface Product {
    id: number;
    title: string;
    image: string;
}

interface ProductCardProps {
    products: Product[];
}

export const ProductCard: React.FC<ProductCardProps> = ({ products }) => {
  return (
    <div className={styles.product_card_container}>
      <div className={styles.product_card_info}>
        <div className={styles.product_card_title}>
          <h2>{products[0].title}</h2>
          <div className={styles.hr_line}></div>
        </div>
        <ul className={styles.product_card_price}>
          <li>
            <span>Разделочные </span>{" "}
          </li>
          <li>
            <span>Туристические </span>
          </li>
          <li>
            <span>Охотничьи </span>
          </li>
        </ul>
      </div>
      <div className={styles.product_card_img}>
        <img src={products[0].image} alt={products[0].title} />
      </div>
    </div>
  );
};
