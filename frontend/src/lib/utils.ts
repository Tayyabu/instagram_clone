export function debounce(func: (...args: any[]) => void, delay: number) {
  let timeOutId: number;

  return (...args: any[]) => {
    if (timeOutId)  clearTimeout(timeOutId);
    timeOutId = setTimeout(() => func(...args), delay);
  };
}
