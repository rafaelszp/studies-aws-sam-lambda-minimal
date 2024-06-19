export const handler = async (event, context) => {
  console.log("EVENT: \n" + JSON.stringify(event, null, 2));
  const data = {
    logStreamName: context.logStreamName,
    name: "Child function"
  }
  return data; 
};